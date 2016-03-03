import zope.interface

import zeit.cms.content.reference

import zeit.campus.interfaces


class TopicpageLink(zeit.cms.related.related.RelatedBase):

    zope.interface.implements(zeit.campus.interfaces.ITopicpageLink)

    topicpagelink = zeit.cms.content.reference.SingleResource(
        '.head.topicpagelink.url', 'related')

    topicpagelink_label = zeit.cms.content.dav.mapProperties(
        zeit.campus.interfaces.ITopicpageLink,
        zeit.cms.interfaces.DOCUMENT_SCHEMA_NS,
        ('topicpagelink_label',))

    topicpagelink_label = zeit.cms.content.property.ObjectPathProperty(
        '.head.topicpagelink.label',
        zeit.campus.interfaces.ITopicpageLink['topicpagelink_label'])
