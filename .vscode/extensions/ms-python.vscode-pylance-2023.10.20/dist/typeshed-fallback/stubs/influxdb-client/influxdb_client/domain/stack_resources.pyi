from _typeshed import Incomplete

class StackResources:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        api_version: Incomplete | None = None,
        resource_id: Incomplete | None = None,
        kind: Incomplete | None = None,
        template_meta_name: Incomplete | None = None,
        associations: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None: ...
    @property
    def api_version(self): ...
    @api_version.setter
    def api_version(self, api_version) -> None: ...
    @property
    def resource_id(self): ...
    @resource_id.setter
    def resource_id(self, resource_id) -> None: ...
    @property
    def kind(self): ...
    @kind.setter
    def kind(self, kind) -> None: ...
    @property
    def template_meta_name(self): ...
    @template_meta_name.setter
    def template_meta_name(self, template_meta_name) -> None: ...
    @property
    def associations(self): ...
    @associations.setter
    def associations(self, associations) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
